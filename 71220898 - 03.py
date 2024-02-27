// User class
public class User {
    protected String nama;
    protected String email;
    protected int uang;

    public User(String nama, String email, int uang) {
        this.nama = nama;
        this.email = email;
        this.uang = uang;
    }

    public void withdraw(int jumlah) {
        // Pengurangan saldo dari uang cash dengan jumlah yang ditarik
        uang -= jumlah;
        // Implementasi transfer dari eWallet ke uang cash sesuai feeWithdraw
        saldo -= (jumlah + feeWithdraw);
    }

    public void generatePIN() {
        // Generate PIN
        // ...
    }

    public void emailConfirmation() {
        // Konfirmasi email dengan mengubah nilai isEmailConfirmed menjadi true
        // ...
    }

    public void getinfo() {
        // Tampilkan informasi user, termasuk saldo dan status email jika belum terkonfirmasi
        // ...
    }
}

// eWallet class
public class eWallet {
    protected User user;
    protected int saldo;
    protected String PIN;

    public eWallet(User user) {
        this.user = user;
        this.saldo = 0;
        this.PIN = user.generatePIN();
    }

    public void topup(int jumlah) {
        // Implementasi topup saldo eWallet dari uang cash, termasuk perhitungan fee
        // ...
    }

    public void transfer(eWallet eWallet, int jumlah) {
        // Implementasi transfer saldo antar eWallet, termasuk perhitungan fee
        // ...
    }

    public void withdraw(int jumlah) {
        // Implementasi withdraw saldo dari eWallet ke uang cash, termasuk perhitungan fee
        // ...
    }

    public void getInfo() {
        // Implementasi untuk menampilkan informasi akun user
        // ...
    }
}

// ShopeePay class
public class ShopeePay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;
    private final int feeWithdraw = 1000;

    public ShopeePay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // Implementasi topup untuk ShopeePay, termasuk perhitungan fee
        // ...
    }

    @Override
    public void transfer(eWallet eWallet, int jumlah) {
        // Implementasi transfer untuk ShopeePay, termasuk perhitungan fee dan delay
        // ...
    }

    @Override
    public void withdraw(int jumlah) {
        // Implementasi withdraw untuk ShopeePay, termasuk perhitungan fee
        // ...
    }

    @Override
    public void getInfo() {
        // Implementasi getInfo untuk menampilkan informasi akun ShopeePay
        // ...
    }
}

// GoPay class
public class GoPay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 0; // No transfer fee for GoPay
    private final int feeWithdraw = 1000;

    public GoPay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // Implementasi topup untuk GoPay, termasuk perhitungan fee
        // ...
    }

    @Override
    public void transfer(eWallet eWallet, int jumlah) {
        // Implementasi transfer untuk GoPay, termasuk perhitungan fee dan delay
        // ...
    }

    @Override
    public void withdraw(int jumlah) {
        // Implementasi withdraw untuk GoPay, termasuk perhitungan fee
        // ...
    }

    @Override
    public void getInfo() {
        // Implementasi getInfo untuk menampilkan informasi akun GoPay
        // ...
    }
}
