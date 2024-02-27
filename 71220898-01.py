// eWallet class
public class eWallet {
    // Implementasi method topup untuk menambah saldo eWallet dari uang cash, termasuk perhitungan fee
    public void topup(int jumlah) {
        // Mengurangi uang cash user dengan jumlah yang ditop up
        user.uang -= jumlah;
        // Menambahkan saldo eWallet dengan jumlah yang ditop up dikurangi feeTopup
        saldo += jumlah - feeTopup;
        System.out.println("Top up sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeTopup + ")");
    }

    // Implementasi method transfer untuk mentransfer saldo antar eWallet, termasuk perhitungan fee
    public void transfer(eWallet eWallet, int jumlah) {
        // Menambah saldo penerima dengan jumlah transfer
        eWallet.saldo += jumlah;
        // Mengurangi saldo pengirim dengan jumlah transfer dan feeTransfer
        saldo -= (jumlah + feeTransfer);
        System.out.println("Transfer saldo sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeTransfer + ")");
    }

    // Implementasi method withdraw untuk menarik saldo dari eWallet ke uang cash, termasuk perhitungan fee
    public void withdraw(int jumlah) {
        // Mengurangi saldo eWallet dengan jumlah yang ditarik dan feeWithdraw
        saldo -= (jumlah + feeWithdraw);
        // Menambah uang cash user dengan jumlah yang ditarik
        user.uang += jumlah;
        System.out.println("Withdraw saldo sebesar Rp" + jumlah + " berhasil! (Fee: Rp" + feeWithdraw + ")");
    }

    // Implementasi method getInfo untuk menampilkan informasi akun user
    public void getInfo() {
        System.out.println("[e-Wallet]");
        System.out.println("Nama: " + user.nama);
        System.out.println("Email: " + user.email);
        System.out.println("Uang cash: Rp" + user.uang);
        System.out.println("Saldo e-wallet: Rp" + saldo);
    }
}
