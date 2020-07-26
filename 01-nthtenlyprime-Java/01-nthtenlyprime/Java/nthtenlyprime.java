class nthtenlyprime {
	public int fun_nthtenlyprime(int n){
		int c = 0;
		int num = 1;
		while(c <= n){
			if(isprime(num)){
				if(istenly(num)){
					c++;
				}
			}
			num++;
		}
		System.out.println(num-1);
		return (num-1);
	}
	public boolean isprime(int n){
		boolean flag = false;
		for(int i = 2; i < n/2; i++){
			if(n%i == 0){
				flag = true;
				break;
			}
		}
		if(!flag){
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
	// public static void main(String[] args) {
	// 	nthtenlyprime ten = new nthtenlyprime();
	// 	ten.fun_nthtenlyprime(0);
	// }
}