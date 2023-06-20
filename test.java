public class test{

    public static void main(String[] args){
        System.out.println("Test....");
    }
    public int findIndex(String str){
        String[] month = {"janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"};
        for(int i=0;i<month.length();i++){
            if(str.equalIgnoreCase(month[i])) return i;
        }
    }

}