#include<iostream>
#include<algorithm>
#define endl '\n'
using namespace std;

bool check(string &a, string &b)

{
    int i = 0, j = 0, n = a.length(), m = b.length();
    while(j < m)
    {
        while(i < n && a[i] != b[j])
            i++;
        if(i == n)
            {
                //printf("%d %d",i,n);
                return true;
            }
        i++;
        j++;
    }
    return false;
}

string conv(int n){
    string res;
    while(n)
    {
        char ch = '0' + n%2;
        res += ch;
        n >>= 1;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main(){

    int tc = 1; 
    cin>>tc;
    for(int t = 0; t < tc; t++)
        {
        string s; 
        cin>>s;
        string ans;
        for(int i = 0; i <= (1<<11); i++)
            {
            string bin;
            if(i == 0)
                bin = "0";
            else 
                {
                    bin = conv(i);
                }
            
            if(check(s, bin))
                {
                ans = bin; 
                break;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
