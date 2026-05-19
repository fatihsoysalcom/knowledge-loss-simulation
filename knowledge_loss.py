import random

class CompanyKnowledge:
    def __init__(self, initial_knowledge_level=100):
        self.knowledge_level = initial_knowledge_level
        self.knowledge_sources = [] # Represents employees, documents, etc.

    def add_knowledge_source(self, source_name):
        self.knowledge_sources.append(source_name)
        print(f"Added knowledge source: {source_name}")

    def simulate_knowledge_loss(self, loss_percentage):
        # Simulates knowledge loss due to employee departure, etc.
        loss_amount = int(self.knowledge_level * (loss_percentage / 100))
        self.knowledge_level = max(0, self.knowledge_level - loss_amount)
        print(f"Simulating {loss_percentage}% knowledge loss. Current knowledge level: {self.knowledge_level}")

    def get_knowledge_level(self):
        return self.knowledge_level

    def get_knowledge_sources_count(self):
        return len(self.knowledge_sources)

def run_simulation():
    print("--- Kurumsal Bilgi Kaybı Simülasyonu ---")

    # Scenario 1: Company relying heavily on individual employees (human memory)
    print("\nSenaryo 1: İnsan Hafızasına Yüksek Bağımlılık")
    company_a = CompanyKnowledge(initial_knowledge_level=100)
    company_a.add_knowledge_source("Ali (Senior Developer)")
    company_a.add_knowledge_source("Ayşe (Project Manager)")
    company_a.add_knowledge_source("Mehmet (Support Lead)")

    print(f"Başlangıç Bilgi Seviyesi (Şirket A): {company_a.get_knowledge_level()}%")
    print(f"Bilgi Kaynak Sayısı (Şirket A): {company_a.get_knowledge_sources_count()}")

    # Simulate a key employee leaving
    print("\nAli işten ayrılıyor...")
    company_a.simulate_knowledge_loss(loss_percentage=30) # Ali held 30% of the knowledge

    print(f"Ali ayrıldıktan sonraki Bilgi Seviyesi (Şirket A): {company_a.get_knowledge_level()}%")

    # Scenario 2: Company with documented knowledge and diverse sources
    print("\nSenaryo 2: Dokümantasyona Dayalı Bilgi Yönetimi")
    company_b = CompanyKnowledge(initial_knowledge_level=100)
    company_b.add_knowledge_source("Dev Docs v1.0")
    company_b.add_knowledge_source("Project Wiki")
    company_b.add_knowledge_source("Support KB")
    company_b.add_knowledge_source("Burak (Developer)")
    company_b.add_knowledge_source("Ceren (QA Lead)")

    print(f"Başlangıç Bilgi Seviyesi (Şirket B): {company_b.get_knowledge_level()}%")
    print(f"Bilgi Kaynak Sayısı (Şirket B): {company_b.get_knowledge_sources_count()}")

    # Simulate a key employee leaving, but knowledge is documented
    print("\nBurak işten ayrılıyor...")
    # Even if Burak leaves, the knowledge is partially retained in other sources
    company_b.simulate_knowledge_loss(loss_percentage=10) # Only 10% loss as knowledge is documented

    print(f"Burak ayrıldıktan sonraki Bilgi Seviyesi (Şirket B): {company_b.get_knowledge_level()}%")

    print("\n--- Simülasyon Sonu ---")
    print("İnsan hafızasına aşırı bağımlılık, bireysel ayrılıklarda büyük bilgi kaybına yol açar.")
    print("Dokümantasyon ve çeşitli bilgi kaynakları, bu riski azaltır.")

if __name__ == "__main__":
    run_simulation()
