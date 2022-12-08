#include <iostream>
#include <math.h>
#include <string>

using namespace std;

bool isPrime(long int prime)
{
    long int i, j;

    j = (long int)sqrt((long double)prime);

    for (i = 2; i <= j; i++)
    {
        if (prime % i == 0)
        {
            return false;
        }
    }

    return true;
}

long int greatestCommonDivisor(long int e, long int t)
{
    while (e > 0)
    {
        long int myTemp;

        myTemp = e;
        e = t % e;
        t = myTemp;
    }

    return t;
}

long int calculateE(long int t)
{
    // Выбирается целое число e ( 1 < e < t ) // взаимно простое со значением функции Эйлера (t)

    long int e;

    for (e = 2; e < t; e++)
    {
        if (greatestCommonDivisor(e, t) == 1)
        {
            return e;
        }
    }

    return -1;
}


long int calculateD(long int e, long int t)
{
    // Вычисляется число d, мультипликативно обратное к числу e по модулю φ(n), то есть число, удовлетворяющее сравнению:
    //    d ⋅ e ≡ 1 (mod φ(n))

    long int d;
    long int k = 1;

    while (1)
    {
        k = k + t;

        if (k % e == 0)
        {
            d = (k / e);
            return d;
        }
    }

}


long int encrypt(long int i, long int e, long int n)
{
    long int current, result;

    current = i - 11;
    result = 1;

    for (long int j = 0; j < e; j++)
    {
        result = result * current;
        result = result % n;
    }

    return result;
}

long int decrypt(long int i, long int d, long int n)
{
    long int current, result;

    current = i;
    result = 1;

    for (long int j = 0; j < d; j++)
    {
        result = result * current;
        result = result % n;
    }

    return result + 11;
}
int main()
{

    long int p, q, n, t, e, d;
    long int encryptedText[100];
    long int decryptedText[100];
    bool flag;
    string msg;

    setlocale(LC_ALL, "Russian");

    // Cоздание открытого и секретного ключей

    // 1. Выбираются два различных случайных простых числа p и q заданного размера

    do
    {
        cout << "Простое число  p :" << endl;
        cin >> p;
        flag = isPrime(p);
    } while (flag == false);


    do
    {
        cout << "Простое число  q :" << endl;
        cin >> q;
        flag = isPrime(q);
    } while (flag == false);

    // 2. Вычисляется их произведение n = p ⋅ q, которое называется модулем.
    n = p * q;
    cout << "\nРезультат умножения n = p*q = " << n << endl;

    // 3. Вычисляется значение функции Эйлера от числа n: φ(n) = (p−1)⋅(q−1)
    t = (p - 1) * (q - 1);
    cout << "Значение функции Эйлера:\t t = " << t << endl;

    // 4. Выбирается целое число e ( 1 < e < φ(n) ), взаимно простое со значением функции Эйлера (t)
    //	  Число e называется открытой экспонентой
    e = calculateE(t);

    // 5. Вычисляется число d, мультипликативно обратное к числу e по модулю φ(n), то есть число, удовлетворяющее сравнению:
    //    d ⋅ e ≡ 1 (mod φ(n))
    d = calculateD(e, t);

    // 6. Пара {e, n} публикуется в качестве открытого ключа RSA
    cout << "\nRSA открытый ключ: (n = " << n << ", e = " << e << ")" << endl;

    // 7. Пара {d, n} играет роль закрытого ключа RSA и держится в секрете
    cout << "RSA закрытый ключ: (n = " << n << ", d = " << d << ")" << endl;



    cout << "\nТекст для шифрования:" << endl;
    cin.ignore();
    getline(cin, msg);

    // encryption

    for (long int i = 0; i < msg.length(); i++)
    {
        encryptedText[i] = encrypt(msg[i], e, n);
    }

    cout << "\nЗашифрованный текст:" << endl;

    for (long int i = 0; i < msg.length(); i++)
    {
        printf("%c", (char)encryptedText[i]);
    }


    //decryption

    for (long int i = 0; i < msg.length(); i++)
    {
        decryptedText[i] = decrypt(encryptedText[i], d, n);
    }

    cout << "\n\nРассшифрованный текст:" << endl;

    for (long int i = 0; i < msg.length(); i++)
    {
        printf("%c", (char)decryptedText[i]);
    }

    cout << endl << endl;

    return 0;
}
