import { Navbar } from "@/components/landing/navbar";
import { Hero } from "@/components/landing/hero";
import { ConversationalSearch } from "@/components/landing/conversational-search";
import { Features } from "@/components/landing/features";
import { HowItWorks } from "@/components/landing/how-it-works";
import { Footer } from "@/components/landing/footer";

export default function Home() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <Navbar />
      <Hero />
      <ConversationalSearch />
      <Features />
      <HowItWorks />
      <Footer />
    </main>
  );
}
