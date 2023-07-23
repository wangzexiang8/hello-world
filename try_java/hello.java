package try_java;
public class hello{
    public static void main(String[] args){
        System.out.println("Hello World!");
        System.out.println("6");
        int a=666;
        System.out.println(a);
        System.out.println("---------------------------------");
        add(25, 1);
        wrong();
    }
    public static void add(int num1,int num2){
        System.out.println(num1+num2);
    }
    public static void dcrease(int num1,int num2){
        System.out.println("=============================");
        dcrease(34, 4);
    }
    public static void wrong(){
        int w;
        w=1;
        System.out.println(w);
    }
}