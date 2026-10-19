import type {Metadata} from 'next';
import './globals.css';
export const metadata:Metadata={title:'Wave Control | Planejamento de Ondas',description:'Ambiente demonstrativo de planejamento operacional de separação, com dados fictícios.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="pt-BR"><body>{children}</body></html>}
