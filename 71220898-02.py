// ShopeePay class
public class ShopeePay extends eWallet {
    private final int feeTopup = 1000;
    private final int feeTransfer = 500;
    private final int feeWithdraw = 1000;

    public ShopeePay(User user) {
        super(user);
    }

    // Implementasi method topup untuk ShopeePay, termasuk perhitungan fee
    @Override
    public void topup(int jumlah) {
        // Mengurangi uang cash user dengan jumlah yang ditop up
        user.uang -= jumlah;
        // Menambahkan saldo eWallet dengan jumlah yang ditop up dikurangi feeTopup
        saldo += jumlah - feeTopup;
        System.out.println("Top up sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeTopup + ")");
    }

    // Implementasi method transfer untuk ShopeePay, termasuk perhitungan fee dan delay
    @Override
    public void transfer(eWallet eWallet, int jumlah) {
        // Menambah saldo penerima dengan jumlah transfer
        eWallet.saldo += jumlah;
        // Mengurangi saldo pengirim dengan jumlah transfer dan feeTransfer
        saldo -= (jumlah + feeTransfer);
        // Menampilkan pesan delay
        System.out.println("Transfer sedang diproses...");
        try {
            // Delay 3 detik
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Transfer saldo sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeTransfer + ")");
    }

    // Implementasi method withdraw untuk ShopeePay, termasuk perhitungan fee
    @Override
    public void withdraw(int jumlah) {
        // Mengurangi saldo eWallet dengan jumlah yang ditarik dan feeWithdraw
        saldo -= (jumlah + feeWithdraw);
        // Menambah uang cash user dengan jumlah yang ditarik
        user.uang += jumlah;
        System.out.println("Withdraw saldo sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeWithdraw + ")");
    }

    // Implementasi method getInfo untuk menampilkan informasi akun ShopeePay
    @Override
    public void getInfo() {
        System.out.println("[ShopeePay e-Wallet]");
        System.out.println("Nama: " + user.nama);
        System.out.println("Email: " + user.email);
        System.out.println("Uang cash: Rp" + user.uang);
        System.out.println("Saldo e-wallet: Rp" + saldo);
    }
}
