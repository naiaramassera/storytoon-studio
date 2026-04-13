import Link from 'next/link'
import { Header } from '../components/Header'

export default function HomePage() {
  return (
    <div>
      <Header />
      <section className="grid gap-6 md:grid-cols-2">
        <div className="card">
          <h2 className="mb-3 text-2xl font-semibold">Crie uma série por prompt</h2>
          <p className="mb-4 text-slate-300">
            Cadastre personagens, defina vozes fixas e transforme uma história inteira em um episódio animado.
          </p>
          <Link href="/series/new" className="btn inline-block">Começar agora</Link>
        </div>
        <div className="card">
          <h3 className="mb-3 text-xl font-semibold">Fluxo do MVP</h3>
          <ol className="space-y-2 text-slate-300">
            <li>1. Criar série</li>
            <li>2. Criar personagens</li>
            <li>3. Colar a história</li>
            <li>4. Gerar outline</li>
            <li>5. Renderizar episódio</li>
          </ol>
        </div>
      </section>
    </div>
  )
}
