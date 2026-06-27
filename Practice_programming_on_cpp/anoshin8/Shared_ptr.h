
#pragma once

template <class T>
class Shared_ptr {
    T* pointer = nullptr;
    size_t* reference_count = nullptr;
public:
    Shared_ptr() {};
    explicit Shared_ptr(const T& obj);
    explicit Shared_ptr(T* const pobj);
    Shared_ptr(const Shared_ptr<T>& rhs);
    ~Shared_ptr();
    Shared_ptr<T>& operator=(const Shared_ptr<T>& rhs);
    size_t GetRefCount() const { return *reference_count; }
    T* operator->() { return pointer; }
    T &operator*() { return *pointer; }
};


template <class T>
Shared_ptr<T>::Shared_ptr(T* const pobj) {
    pointer = pobj;
    reference_count = new size_t(1);
}

template <class T>
Shared_ptr<T>::Shared_ptr(const T& obj) {
    pointer = new T(obj);
    reference_count = new size_t(1);
}

template <class T>
Shared_ptr<T>::Shared_ptr(const Shared_ptr<T>& rhs) {
    pointer = rhs.pointer;
    reference_count = rhs.reference_count;
    ++(*reference_count);
}

template <class T>
Shared_ptr<T>::~Shared_ptr() {
    if (reference_count) {
        --(*reference_count);
        if (*reference_count == 0) {
            delete reference_count;
            delete pointer;
        }
    }
}

template <class T>
Shared_ptr<T>& Shared_ptr<T>::operator=(const Shared_ptr<T>& rhs) {
    if (this == &rhs) {
        return *this;
    }
    if (reference_count) {
        --(*reference_count);
        if (*reference_count) {
            delete reference_count;
            delete pointer;
        }
    }
    reference_count = rhs.reference_count;
    pointer = rhs.pointer;
    if (reference_count) {
        ++(*reference_count);
    }
    return *this;
}


template <class T, class... Args>
Shared_ptr<T> MakeShared(Args... args) {
    auto* pointer = new T(args...);
    return Shared_ptr<T>(pointer);
}

