package colourtablemanagement;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ColourTest {
    @Test
        // check if object is null after construction
    void checkIfNull() {
        Colour testColour = new Colour(255, 0, 0);
        assertNotNull(testColour);
    }

    @Test
        // check if constructor is assigning values correctly
    void checkIfCorrectValues() {
        Colour testColour = new Colour(147, 59, 72);
        assertEquals(147, testColour.getRed());
        assertEquals(59, testColour.getGreen());
        assertEquals(72, testColour.getBlue());
    }

    @Test
        // check if inputted values are in specified range
    void checkIfInRange() {
        Colour testColour = new Colour(155, 156, 157);

        // checks to see if assigns correctly when values in range
        assertEquals(155, testColour.getRed());
        assertEquals(156, testColour.getGreen());
        assertEquals(157, testColour.getBlue());


        // check to see if exception is thrown if any rgb value is out of range
        assertThrows(IllegalArgumentException.class, () -> new Colour(256, 0, 0));
        assertThrows(IllegalArgumentException.class, () -> new Colour(0, -55, 0));
        assertThrows(IllegalArgumentException.class, () -> new Colour(0, 0, 1000));
    }

    @Test
        // check if the equals method is functioning correctly
    void checkIfEquals() {
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);
        Colour red_2 = new Colour(255, 0, 0);
        Colour green_2 = new Colour(0, 255, 0);

        assertTrue(red.equals(red_2));
        assertTrue(green.equals(green_2));
        assertFalse(red.equals(green));
        assertFalse(green_2.equals(red_2));
    }

    @Test
        // check if exception is thrown if no argument is called
    void checkIfNoArgument() {
        assertThrows(IllegalArgumentException.class, () -> new Colour());
    }

    @Test
        // test to check the toString() method of my colour representation
    void checkToStringRepresentation() {
        Colour red = new Colour(255, 255, 0);
        assertEquals("Colour {\n\tR= 255\n\tG= 255\n\tB= 0\n\tHEX= ff ff 0\n}\n", red.toString());
    }
}
