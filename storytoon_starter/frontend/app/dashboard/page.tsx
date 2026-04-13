import Link from 'next/link'
import { Header } from '../../components/Header'

export default function DashboardPage() {
  return (
    <div>
      <Header />
      <div className="grid gap-6 md:grid-cols-3">
        <div className="card">
          <p className="text-sm text-slate-400">Séries</p>
          <p className="mt-2 text-3xl font-bold">0</p>
        </div>
        <div className="card">
          <p className="text-sm text-slate-400">Episódios</p>
          <p className="mt-2 text-3xl font-bold">0</p>
        </div>
        <div className="card">
          <p className="text-sm text-slate-400">Minutos do plano</p>
          <p className="mt-2 text-3xl font-bold">200</p>
        </div>
      </div>
      <div className="mt-6 card">
        <h2 className="text-xl font-semibold">Ações rápidas</h2>
        <div className="mt-4 flex gap-3">
          <Link href="/series/new" className="btn">Nova série</Link>
          <Link href="/episodes/new" className="rounded-xl border border-slate-700 px-4 py-3">Novo episódio</Link>
        </div>
      </div>
    </div>
  )
}
