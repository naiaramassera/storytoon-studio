import Link from 'next/link'

export function Header() {
  return (
    <header className="mb-8 flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold">StoryToon Studio</h1>
        <p className="text-slate-400">Séries com personagens persistentes e episódios automáticos.</p>
      </div>
      <nav className="flex gap-3 text-sm">
        <Link href="/dashboard" className="rounded-xl border border-slate-700 px-4 py-2">Dashboard</Link>
        <Link href="/series/new" className="rounded-xl border border-slate-700 px-4 py-2">Nova série</Link>
        <Link href="/episodes/new" className="btn">Novo episódio</Link>
      </nav>
    </header>
  )
}
