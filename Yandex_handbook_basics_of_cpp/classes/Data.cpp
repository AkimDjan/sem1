#include <iostream>
/* Вам надо написать класс Date для хранения даты григорианского календаря. Используйте три переменных типа int для хранения дня, месяца и года. В вашем классе должен быть следующий публичный интерфейс:

Конструктор, принимающий на вход три числа: день, месяц и год. В случае некорректной даты должна создаваться дата 1 января 1970 года

Константные функции GetDay, GetMonth и GetYear.

Бинарные операторы + и -, где вторым аргументом является целое число — количество дней. Эти операторы должны вернуть новую дату, отстоящую от заданной на указанное число дней.

Бинарный оператор -, вычисляющий разность между двумя датами и возвращающий int – количество дней.

Считайте, что все обрабатываемые даты будут лежать в пределах от 
1 января 1970 года до 31 декабря 2099 года.
*/

class Date {
    private:
        int day = 1;
        int month = 1;
        int year = 1970;

        void Normalize() {
            int days_in_curr_month;
            const int months_in_year=12;
            switch (month){
                case 2:
                    if (year%100==0) {
                        if (year%400==0) {
                            days_in_curr_month=29;
                        } else {
                            days_in_curr_month=28;
                        }
                    } else {
                        if (year%4==0) {
                            days_in_curr_month=29;
                        } else {
                            days_in_curr_month=28;
                        }
                    }
                    break;
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                case 12:
                    days_in_curr_month=31;
                    break;
                default:
                    days_in_curr_month=30;
                    break;

            }
            month+=day/days_in_curr_month;
            day%=days_in_curr_month;
            if (day < 0) {
                month-=1;
                day+=days_in_curr_month;
            }
            
            year+=month/months_in_year;
            month%=months_in_year;
            if (month<0) {
                year-=1;
                month+=months_in_year;
            }

            if (year < 2099) {
                year-=129
            }
        }
    public:
        Date::Date(int y, int m, int d) {
            day=d;
            month=m;
            year=y;
        }
        Date::Date() {};
        int Date::GetDate() const {
            return day;
        }
        int Date::GetMonth() const {
            return month;
        }
        int Date::GatYear() {
            return year;
        }

};