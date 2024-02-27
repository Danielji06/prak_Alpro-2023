// User.java
public class User {
    private String nama;
    private String email;
    private int uang;
    private String PIN;
    private boolean isEmailConfirmed;

    public User(String nama, String email, int uang) {
        this.nama = nama;
        this.email = email;
        this.uang = uang;
        this.isEmailConfirmed = false;
        this.PIN = generatePIN();
    }

    public void emailConfirmation() {
        this.isEmailConfirmed = true;
        System.out.println("Email berhasil dikonfirmasi!");
    }

    public void generatePIN() {
        // Implementasi generatePIN() sesuai kebutuhan
    }

    // Getter dan setter lainnya sesuai kebutuhan
}

// eWallet.java
public class eWallet {
    private User user;
    private int saldo;

    public eWallet(User user) {
        this.user = user;
        this.saldo = 0;
    }

    public void topup(int jumlah) {
        // Implementasi topup() sesuai kebutuhan
    }

    public void transfer(eWallet tujuan, int jumlah) {
        // Implementasi transfer() sesuai kebutuhan
    }

    public void withdraw(int jumlah) {
        // Implementasi withdraw() sesuai kebutuhan
    }

    public void getInfo() {
        // Implementasi getInfo() sesuai kebutuhan
    }

    // Getter dan setter lainnya sesuai kebutuhan
}

// ShopeePay.java
public class ShopeePay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;

    public ShopeePay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // Implementasi topup() untuk ShopeePay sesuai kebutuhan
    }

    @Override
    public void transfer(eWallet tujuan, int jumlah) {
        // Implementasi transfer() untuk ShopeePay sesuai kebutuhan
    }

    @Override
    public void withdraw(int jumlah) {
        // Implementasi withdraw() untuk ShopeePay sesuai kebutuhan
    }

    @Override
    public void getInfo() {
        // Implementasi getInfo() untuk ShopeePay sesuai kebutuhan
    }
}

// GoPay.java
public class GoPay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;
    private final int feeWithdraw = 1000;

    public GoPay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // Implementasi topup() untuk GoPay sesuai kebutuhan
    }

    @Override
    public void transfer(eWallet tujuan, int jumlah) {
        // Implementasi transfer() untuk GoPay sesuai kebutuhan
    }

    @Override
    public void withdraw(int jumlah) {
        // Implementasi withdraw() untuk GoPay sesuai kebutuhan
    }

    @Override
    public void getInfo() {
        // Implementasi getInfo() untuk GoPay sesuai kebutuhan
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        // Implementasi pengujian sesuai kebutuhan
    }
}
