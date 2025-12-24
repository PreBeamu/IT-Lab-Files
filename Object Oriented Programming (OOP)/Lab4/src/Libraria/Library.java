/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Libraria;

/**
 *
 * @author prebe
 */
public class Library {

    public String libraryName;
    public Book book1;
    public Book book2;
    public Book book3;

    public void addBook(Book book, int slot) {
        switch (slot) {
            case 1 ->
                book1 = book;
            case 2 ->
                book2 = book;
            case 3 ->
                book3 = book;
        }
    }

    public void removeBook(int slot) {
        switch (slot) {
            case 1 ->
                book1 = null;
            case 2 ->
                book2 = null;
            case 3 ->
                book3 = null;
        }
    }

    public void printLibraryDetails() {
        System.out.println("Library: " + libraryName);
        System.out.println("");
        for (int i = 1; i <= 3; i++) {
            Book currBook = null;
            switch (i) {
                case 1 ->
                    currBook = book1;
                case 2 ->
                    currBook = book2;
                case 3 ->
                    currBook = book3;
            }
            if (currBook != null) {
                currBook.printDetails();
            } else {
                System.out.println("No book in this slot.");
            }
            System.out.println("");
        }
    }

    public void checkBookAvailability(int slot) {
        Book currBook = null;
        switch (slot) {
            case 1 ->
                currBook = book1;
            case 2 ->
                currBook = book2;
            case 3 ->
                currBook = book3;
        }
        if (currBook != null) {
            System.out.println(currBook.title + " is available.");
        } else {
            System.out.println("Book in slot " + slot + " is not available.");
        }
    }

    public void updateBookPrice(int slot, double newPrice) {
        Book currBook = null;
        switch (slot) {
            case 1 ->
                currBook = book1;
            case 2 ->
                currBook = book2;
            case 3 ->
                currBook = book3;
        }
        if (currBook != null) {
            currBook.price = newPrice;
            System.out.println("Updated price of " + currBook.title + " to $" + currBook.price + ".");
        } else {
            System.out.println("No book in this slot.");
        }
    }

    public void printBookDetails(Book book) {
        book.printDetails();
    }
}
