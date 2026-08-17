package colourtablemanagement;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ColourTableTest {

    @Test
    // check if object is not null after initialisation
    void checkIfNull() {
        ColourTable testTable = new ColourTable(8);
        assertNotNull(testTable);
    }

    @Test
    // check if colour table size meets requirements (is a power of 2 and less than 1025)
    void checkIfCorrectPaletteSize () {
        ColourTable test1 = new ColourTable(2);
        ColourTable test2 = new ColourTable(8);

        // checks to see if size satisfies requirements array of that size is created
        assertEquals(2, test1.getPaletteSize());
        assertEquals(8, test2.getPaletteSize());

        // checks if exception is thrown for invalid palette sizes
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(0));
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(10000));
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(7));
    }

    @Test
    // check if exception is thrown if colourTable is called without a palette size
    void checkForPaletteSizeInput() {
        assertThrows(IllegalArgumentException.class, () -> new ColourTable());
    }

    @Test
    // test method to count number of empty spaces in colour palette
    void checkForEmptyPaletteSpace () {
        ColourTable test = new ColourTable(1024);
        assertEquals(test.getPaletteSize(), test.getFreePaletteSpace());
        assertEquals(1024, test.getFreePaletteSpace());
    }

    @Test
    // method to test if colour is being added
    void checkIfColourAdded() {
        ColourTable test = new ColourTable(2);
        Colour red = new Colour(255, 0, 0);
        test.add(red);
        assertEquals(red, test.getColourAtIndex(0));
    }

    @Test
    // test to see if colours are only added at null indexes
    void checkIfOnlyAddedAtNull() {
        ColourTable test = new ColourTable(4);
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);

        assertNull(test.getColourAtIndex(0));
        assertNull(test.getColourAtIndex(1));
        assertNull(test.getColourAtIndex(2));
        assertNull(test.getColourAtIndex(3));

        test.add(red);
        test.add(green);

        assertEquals(red, test.getColourAtIndex(0));
        assertEquals(green, test.getColourAtIndex(1));
        assertNull(test.getColourAtIndex(2));
        assertNull(test.getColourAtIndex(3));
    }

    @Test
    // method to check if IllegalStateException is thrown if colour is added out of bound or there is no free space
    void checkIfColourCanBeAdded() {
        ColourTable test = new ColourTable(2);
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);
        Colour blue = new Colour(0, 0, 255);

        test.add(red);
        test.add(green);

        assertThrows(IllegalStateException.class, () -> test.add(blue));
    }

    @Test
    // method to check functionality of contains method
    void checkIfContains() {
        ColourTable test = new ColourTable(2);
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);
        Colour blue = new Colour(0, 0, 255);

        test.add(red);
        test.add(green);

        assertTrue(test.contains(red));
        assertTrue(test.contains(green));
        assertTrue(test.contains(new Colour(255,0 ,0)));
        assertFalse(test.contains(blue));
    }

    @Test
    // method to check if colour is only added if not already in the palette
    void onlyAddIfNotInPalette() {
        ColourTable test = new ColourTable(2);
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);

        test.add(red);
        assertThrows(IllegalArgumentException.class, () -> test.add(red));
        assertTrue(test.contains(red));
        test.add(green);
        assertTrue(test.contains(green));
    }

    @Test
    // method to check if the toString() method of ColourTable is working properly
    void checkToStringRepresentation() {
        ColourTable test = new ColourTable(4);
        Colour red = new Colour(255, 0, 0);
        Colour green = new Colour(0, 255, 0);
        test.add(red);
        test.add(green);
        assertEquals("""
                Colour Palette {

                \tTotal Palette Size: 4
                \tNo. of Colours in Palette: 2
                \tFree Palette Space: 2
                \tColours:
                \t\tColour {
                \t\t\tR= 255
                \t\t\tG= 0
                \t\t\tB= 0
                \t\t\tHEX= ff 0 0
                \t\t}
                \t\tColour {
                \t\t\tR= 0
                \t\t\tG= 255
                \t\t\tB= 0
                \t\t\tHEX= 0 ff 0
                \t\t}
                }""", test.toString());
    }
}
