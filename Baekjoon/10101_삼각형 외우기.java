import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> angleSet = new HashSet<Integer>();
        int sumOfAngles = 0;
        for (int i=0; i<3; i++) {
            int angle = Integer.parseInt(br.readLine());
            sumOfAngles += angle;
            angleSet.add(angle);
        }
        br.close();

        int angleSetSize = angleSet.size();
        if (sumOfAngles == 180) {
            if (angleSetSize == 1) {
                System.out.println("Equilateral");
            } else if (angleSetSize == 2) {
                System.out.println("Isosceles");
            } else {
                System.out.println("Scalene");
            }
        } else {
            System.out.println("Error");
        }
    }
}
