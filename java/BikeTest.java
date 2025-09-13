import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BikeTest {
    @Test
    public void TestTheDefaultStateOfTheBike() {

        Bike bike = new Bike();
        assertFalse(bike.getPower());
    }

    @Test
    public void TestIfTheBikeIsOn() {
        Bike bike = new Bike();
        bike.start();
        assertTrue(bike.getPower());
    }

    @Test
    public void TestIfTheBikeCanTUrnOnAndOff() {
        Bike bike = new Bike();
        bike.start();
        bike.stop();
        assertFalse(bike.getPower());
    }

    @Test
    public void TestForTheCurrentGear() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(1);

        assertEquals(1, bike.getGear());
    }

    @Test
    public void TestIfTheBikeWillChangeGearWhenOff() {
        Bike bike = new Bike();
        bike.start();
        bike.stop();

        assertEquals(0, bike.getGear());
    }

    @Test
    public void Test() {

    }

    @Test
    public void TestForAcceleration() {
        Bike bike = new Bike();
        bike.setAccelerate();

        assertEquals(0, bike.getAcceleration());
    }

    @Test
    public void testForWhenTheBikeIsOnAndAccelerate() {
        Bike bike = new Bike();
        bike.start();
        bike.setAccelerate();

        assertEquals(0, bike.getAcceleration());

    }

    @Test
    public void TestAccelerationWhenTheBikeIsOnAndGearOne() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(1);
        bike.setAccelerate();

        assertEquals(1, bike.getAcceleration());

    }

    @Test
    public void TestAccelerationWhenTheBikeIsOnAndGearTwo() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(2);
        bike.setAccelerate();
        assertEquals(2, bike.getAcceleration());
    }

    @Test
    public void TestForWhenTheBikeIsOnAndGearThree() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(3);
        bike.setAccelerate();
        assertEquals(3, bike.getAcceleration());
    }

    @Test
    public void TestForWhenTheBikeIsOffAndGearFour() {
        Bike bike = new Bike();
        bike.start();
        bike.stop();
        bike.setGear(4);
        bike.setAccelerate();
        assertEquals(0, bike.getAcceleration());

    }

    @Test
    public void TestForAccelerationIncrementWithTheCurrentGear() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(4);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();

        assertEquals(12, bike.getAcceleration());

    }

    @Test
    public void TestIfTheGearExcceds4() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(5);
        bike.setAccelerate();

        assertEquals(0, bike.getGear());
        assertEquals(0, bike.getAcceleration());
    }
    @Test
    public void TestIfTheGearDoestNotReachUpTo0() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(-3);
        bike.setAccelerate();

        assertEquals(0, bike.getGear());
        assertEquals(0, bike.getAcceleration());
    }

    @Test
    public void TestIfTheTheCurrentGearWillChangeWhenAccelerationExceed20() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(1);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();

        assertEquals(21, bike.getAcceleration());
        assertEquals(2, bike.getGear());
    }

    @Test
    public void TestIfTheTheCurrentGearWillChangeWhenAccelerationExceed30() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(2);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();

        assertEquals(32, bike.getAcceleration());
        assertEquals(3, bike.getGear());
    }

    @Test
    public void TestIfTheTheCurrentGearWillChangeWhenAccelerationExceed40() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(3);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();

        assertEquals(42, bike.getAcceleration());
        assertEquals(4, bike.getGear());

    }

    @Test
    public void TestIfTheTheCurrentGearWillChangeWhenAccelerationExceed41() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(4);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();


        assertEquals(56, bike.getAcceleration());
        assertEquals(4, bike.getGear());
    }

@Test
    public void TestIfDecelerationDecreaseWithCurrentGear1() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(1);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(1,bike.getAcceleration());
}
@Test
    public void TestIfDecelerationDecreaseWithCurrentGear2() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(2);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(2,bike.getAcceleration());
}
@Test
    public void TestIfDecelerationDecreaseWithCurrentGear4() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(4);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(4,bike.getAcceleration());
}
@Test
    public void TestIfDecelerationDidNotDecreaseWithCurrentGear7() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(7);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();

        assertEquals(0,bike.getAcceleration());
        assertEquals(0,bike.getGear());

}
@Test
    public void TestIfCurrentGearChangesWhenDecelerationDecreaseTo40() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(4);
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setAccelerate();
    bike.setDeceleration();

    assertEquals(40, bike.getAcceleration());
    assertEquals(3, bike.getGear());


}
@Test
    public void TestIfCurrentGearChangesWhenDecelerationDecreaseTo30() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(3);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(18, bike.getAcceleration());
        assertEquals(2, bike.getGear());
}
    @Test
    public void TestIfCurrentGearChangesWhenDecelerationDecreaseTo20() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(2);
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(20, bike.getAcceleration());
        assertEquals(1, bike.getGear());
    }
@Test
    public void TestIfCurrentGearChangesWhenDecelerationDecreaseTo0() {
        Bike bike = new Bike();
        bike.start();
        bike.setGear(1);
        bike.setAccelerate();
        bike.setDeceleration();

        assertEquals(0, bike.getAcceleration());
        assertEquals(0, bike.getGear());
}
}