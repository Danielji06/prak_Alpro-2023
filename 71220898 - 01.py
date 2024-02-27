// Class User (provided)
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
        // implementation
    }

    public void generatePIN() {
        // implementation
    }

    public void emailConfirmation() {
        // implementation
    }

    public void getinfo() {
        // implementation
    }
}

// Class eWallet
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
        // implementation
    }

    public void transfer(eWallet eWallet, int jumlah) {
        // implementation
    }

    public void withdraw(int jumlah) {
        // implementation
    }

    public void getInfo() {
        // implementation
    }
}

// Class ShopeePay
public class ShopeePay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;

    public ShopeePay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // implementation
    }

    @Override
    public void transfer(eWallet eWallet, int jumlah) {
        // implementation
    }

    @Override
    public void withdraw(int jumlah) {
        // implementation
    }

    @Override
    public void getInfo() {
        // implementation
    }
}

// Class GoPay
public class GoPay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;
    private final int feeWithdraw = 1000;

    public GoPay(User user) {
        super(user);
    }

    @Override
    public void topup(int jumlah) {
        // implementation
    }

    @Override
    public void transfer(eWallet eWallet, int jumlah) {
        // implementation
    }

    @Override
    public void withdraw(int jumlah) {
        // implementation
    }

    @Override
    public void getInfo() {
        // implementation
    }
}
