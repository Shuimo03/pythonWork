def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)

if __name__ == "__main__":
    a = 122
    b = 68
    print(gcd(a,b))
    pass
[
    {
        id: 1,
        lat: ''
    },
    {
        id:2,
        lat: '2'
    }
]