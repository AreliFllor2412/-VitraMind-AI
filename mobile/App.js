import { useMemo, useState } from "react";
import AuthenticatedLayout from "@/Layouts/AuthenticatedLayout";
import { Head, Link, router } from "@inertiajs/react";
import {
    Eye,
    FileText,
    Pencil,
    Plus,
    Search,
    Trash2,
    CheckCircle2,
    Layers3,
} from "lucide-react";

const certificateTypeLabels = {
    auto: "Automático",
    general: "NEW Cert Gral",
    sin_punto_fusion: "Sin punto de fusión",
    sin_gel_time: "Sin gel time",
    weathering: "AAMA 2604 Weathering",
    hill_phoenix: "Hill Phoenix",
    polvos_moteados: "Polvos moteados",
    methode_psg: "Methode PSG",
};

function getCertificateType(certificado) {
    const type =
        certificado?.plantilla ||
        certificado?.datos?.manualTemplate ||
        "auto";

    return certificateTypeLabels[type] || String(type).replaceAll("_", " ");
}

export default function Index({ auth, certificados = { data: [] } }) {
    const [search, setSearch] = useState("");

    const rows = Array.isArray(certificados)
        ? certificados
        : certificados?.data || [];

    const filteredRows = useMemo(() => {
        const value = search.trim().toLowerCase();

        if (!value) return rows;

        return rows.filter((item) => {
            const text = [
                item?.code,
                item?.producto,
                item?.nombre_cliente,
                item?.lote,
                getCertificateType(item),
            ]
                .filter(Boolean)
                .join(" ")
                .toLowerCase();

            return text.includes(value);
        });
    }, [rows, search]);

    const destroy = (certificado) => {
        const id = certificado?.id;

        if (!id) {
            alert("No se pudo identificar el certificado.");
            return;
        }

        if (!confirm(`¿Eliminar certificado ${certificado?.code || id}?`)) return;

        router.delete(
            route("admin.calidad.certificados.destroy", {
                certificado: id,
            }),
            { preserveScroll: true }
        );
    };

    return (
        <AuthenticatedLayout auth={auth}>
            <Head title="Certificados" />

            <main className="min-h-screen bg-[#F6F9FC] px-4 py-6 sm:px-6 lg:px-8">
                <div className="mx-auto max-w-7xl space-y-5">
                    <section className="rounded-3xl border border-blue-100 bg-white p-5 shadow-sm">
                        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                            <div className="flex items-center gap-4">
                                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-blue-50 text-[#135491]">
                                    <FileText size={27} />
                                </div>

                                <div>
                                    <p className="text-xs font-bold uppercase tracking-[0.18em] text-[#135491]">
                                        Calidad
                                    </p>

                                    <h1 className="text-2xl font-black text-slate-900">
                                        Certificados
                                    </h1>

                                    <p className="text-sm text-slate-500">
                                        Registra, consulta y administra certificados de calidad.
                                    </p>
                                </div>
                            </div>

                            <Link
                                href={route("admin.calidad.NEW_Cert_Gral")}
                                className="inline-flex items-center justify-center gap-2 rounded-xl bg-[#135491] px-5 py-2.5 text-sm font-bold text-white shadow-sm transition hover:bg-[#0f4679] active:scale-95"
                            >
                                <Plus size={17} />
                                Nuevo certificado
                            </Link>
                        </div>
                    </section>

                    <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                        <MiniCard
                            icon={<FileText size={20} />}
                            title="Total"
                            value={rows.length}
                            description="Certificados registrados"
                        />

                        <MiniCard
                            icon={<Layers3 size={20} />}
                            title="Filtrados"
                            value={filteredRows.length}
                            description="Resultados visibles"
                        />

                        <MiniCard
                            icon={<CheckCircle2 size={20} />}
                            title="Estado"
                            value="Activo"
                            description="Sistema disponible"
                        />
                    </section>

                    <section className="overflow-hidden rounded-3xl border border-blue-100 bg-white shadow-sm">
                        <div className="flex flex-col gap-4 border-b border-slate-100 px-5 py-4 lg:flex-row lg:items-center lg:justify-between">
                            <div>
                                <h2 className="text-base font-black text-slate-900">
                                    Lista de certificados
                                </h2>

                                <p className="text-sm text-slate-500">
                                    Busca por clave, producto, cliente, lote o tipo.
                                </p>
                            </div>

                            <div className="relative w-full lg:max-w-sm">
                                <Search
                                    size={17}
                                    className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
                                />

                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder="Buscar certificado..."
                                    className="w-full rounded-xl border border-blue-100 bg-white py-2.5 pl-10 pr-4 text-sm font-semibold text-slate-700 outline-none transition placeholder:text-slate-400 focus:border-[#135491] focus:ring-4 focus:ring-blue-100"
                                />
                            </div>
                        </div>

                        <div className="overflow-x-auto">
                            <table className="w-full min-w-[950px] text-sm">
                                <thead>
                                    <tr className="bg-blue-50 text-left text-xs font-bold uppercase tracking-wide text-[#135491]">
                                        <th className="px-5 py-3">Clave</th>
                                        <th className="px-5 py-3">Producto</th>
                                        <th className="px-5 py-3">Cliente</th>
                                        <th className="px-5 py-3">Lote</th>
                                        <th className="px-5 py-3">Tipo</th>
                                        <th className="px-5 py-3 text-right">Acciones</th>
                                    </tr>
                                </thead>

                                <tbody className="divide-y divide-slate-100">
                                    {filteredRows.length === 0 ? (
                                        <tr>
                                            <td colSpan="6" className="px-5 py-14 text-center">
                                                <div className="mx-auto flex max-w-sm flex-col items-center">
                                                    <div className="mb-3 flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-50 text-[#135491]">
                                                        <FileText size={28} />
                                                    </div>

                                                    <p className="font-bold text-slate-800">
                                                        No se encontraron certificados
                                                    </p>

                                                    <p className="mt-1 text-sm text-slate-500">
                                                        Prueba con otra clave, cliente, lote o producto.
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                    ) : (
                                        filteredRows.map((certificado) => (
                                            <tr
                                                key={certificado.id}
                                                className="transition hover:bg-blue-50/50"
                                            >
                                                <td className="px-5 py-4">
                                                    <Badge>{certificado.code || "Sin clave"}</Badge>
                                                </td>

                                                <td className="px-5 py-4">
                                                    <p className="max-w-[320px] truncate font-bold text-slate-900">
                                                        {certificado.producto || "Sin producto"}
                                                    </p>
                                                </td>

                                                <td className="px-5 py-4 text-slate-600">
                                                    {certificado.nombre_cliente || "Sin cliente"}
                                                </td>

                                                <td className="px-5 py-4 text-slate-600">
                                                    {certificado.lote || "Sin lote"}
                                                </td>

                                                <td className="px-5 py-4">
                                                    <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-bold text-slate-700">
                                                        {getCertificateType(certificado)}
                                                    </span>
                                                </td>

                                                <td className="px-5 py-4">
                                                    <div className="flex justify-end gap-2">
                                                        <IconLink
                                                            href={route(
                                                                "admin.calidad.certificados.show",
                                                                certificado.id
                                                            )}
                                                            icon={<Eye size={15} />}
                                                            label="Ver"
                                                            color="blue"
                                                        />

                                                        <IconLink
                                                            href={route(
                                                                "admin.calidad.certificados.edit",
                                                                certificado.id
                                                            )}
                                                            icon={<Pencil size={15} />}
                                                            label="Editar"
                                                            color="amber"
                                                        />

                                                        <button
                                                            type="button"
                                                            onClick={() => destroy(certificado)}
                                                            className="inline-flex items-center gap-1 rounded-xl bg-red-50 px-3 py-2 text-xs font-bold text-red-700 transition hover:bg-red-600 hover:text-white active:scale-95"
                                                        >
                                                            <Trash2 size={15} />
                                                            Eliminar
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                        ))
                                    )}
                                </tbody>
                            </table>
                        </div>
                    </section>

                    {certificados?.links && <Pagination links={certificados.links} />}
                </div>
            </main>
        </AuthenticatedLayout>
    );
}

function MiniCard({ icon, title, value, description }) {
    return (
        <div className="rounded-2xl border border-blue-100 bg-white p-4 shadow-sm">
            <div className="flex items-center justify-between">
                <div>
                    <p className="text-xs font-bold uppercase tracking-wide text-slate-500">
                        {title}
                    </p>

                    <p className="mt-1 text-xl font-black text-slate-900">
                        {value}
                    </p>
                </div>

                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-50 text-[#135491]">
                    {icon}
                </div>
            </div>

            <p className="mt-2 text-xs font-medium text-slate-500">
                {description}
            </p>
        </div>
    );
}

function Badge({ children }) {
    return (
        <span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-bold text-[#135491]">
            {children}
        </span>
    );
}

function IconLink({ href, icon, label, color = "blue" }) {
    const colors = {
        blue: "bg-blue-50 text-[#135491] hover:bg-[#135491] hover:text-white",
        amber: "bg-amber-50 text-amber-700 hover:bg-amber-500 hover:text-white",
    };

    return (
        <Link
            href={href}
            className={`inline-flex items-center gap-1 rounded-xl px-3 py-2 text-xs font-bold transition active:scale-95 ${colors[color]}`}
        >
            {icon}
            {label}
        </Link>
    );
}

function Pagination({ links }) {
    return (
        <div className="flex flex-wrap justify-end gap-2">
            {links.map((link, index) => (
                <Link
                    key={`${link.label}-${index}`}
                    href={link.url || "#"}
                    preserveScroll
                    className={`rounded-xl border px-3 py-1.5 text-sm font-bold transition ${
                        link.active
                            ? "border-[#135491] bg-[#135491] text-white"
                            : "border-blue-100 bg-white text-slate-600 hover:bg-blue-50 hover:text-[#135491]"
                    } ${!link.url ? "pointer-events-none opacity-40" : ""}`}
                    dangerouslySetInnerHTML={{ __html: link.label }}
                />
            ))}
        </div>
    );
}
