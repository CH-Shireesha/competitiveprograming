class nthtenlyprime {
	public int fun_nthtenlyprime(int n){
		int c = 0;
		int num = 1;
		while(c <= num){
			if(isprime(num)){
				if(istenly(num)){
					c = c++;
				}
			}
			num = num++;
		}
		return (num-1);
	}
	public boolean isprime(int n){
		int i = 0;
		int c = 0;
		while(c <= n){
			if(n%i == 0){
				c = c++;
				if(c > 2);
					break;
			}
		}
		if(c == 2){
			return true;
		}
		return false;
	}
	public boolean istenly(int n){
		int sum = 0;
		while(n > 0){
			int res = n%10;
			sum = sum + res;
			n = n/10;
		}
		if(sum == 10){
			return true;
		}
		return false;
	}
}