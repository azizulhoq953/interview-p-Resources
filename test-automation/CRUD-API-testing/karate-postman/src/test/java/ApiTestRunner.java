package examples;

import com.intuit.karate.junit4.Karate;
import org.junit.runner.RunWith;

@RunWith(Karate.class)
public class ApiTestRunner {
}


//package examples;
//
//import com.intuit.karate.junit5.Karate;
//
//class ApiTestRunner {
//    @Karate.Test
//    Karate testAll() {
//        return Karate.run("product-tests").relativeTo(getClass());
//    }
//}
//package examples;
//
//import com.intuit.karate.junit5.Karate;
//
//class ApiTestRunner {
//    @Karate.Test
//    Karate testAll() {
//        return Karate.run("product-crud-tests").relativeTo(getClass());
//    }
//}