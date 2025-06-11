import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <header>
          <h1>Ceiling Height Prediction Tool</h1>
        <p>Please choose a date to display a prediction for Ted Stevens Anchorage International Airport (PANC)</p>
        </header>
        {/*interactive inputs */}
        <section>
          {/* TODO: date picker here*/}
        </section>
        {/*visualizations*/}
        <section>
          {/* TODO: graphs from PyMC here */}
        </section>
      </main>
      <footer className={styles.footer}>
        <p>Bayesian regression learning model created by Cynthia Black using PyMC &copy 2025</p>
      </footer>
    </div>
  );
}
