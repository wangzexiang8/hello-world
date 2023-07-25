
public class fangfa{
    public static void main(String[] args){
        fangfa_input javain = new fangfa_input();
        int a=javain.return_input();
        int b=javain.return_input();
        System.out.print(a);
        System.out.print(" ");
        System.out.print(b);
        System.out.print('\n');
        System.out.print("max:");
        System.out.println(max(a, b));
    }
    public static int max(int x,int y){
        if(x>y){
            return x;
        }
        else if(x<y){
            return y;
        }
        else{
            return x;
        }
    }
}