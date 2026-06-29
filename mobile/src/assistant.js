import AuthenticatedLayout from "@/Layouts/AuthenticatedLayout";
import { Head, Link, router } from "@inertiajs/react";
import { Eye, FileText, Pencil, Plus, Trash2 } from "lucide-react";

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

    return certificateTypeLabels[type] || type.replaceAll("_", " ").toUpperCase();
}

export default function Index({ auth, certificados = { data: [] } }) {
    const rows = Array.isArray(certificados)
        ? certificados
        : certificados?.data || [];

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

            <main className="min-h-screen bg-[#F7FAFC] px-4 py-6 sm:px-6 lg:px-8">
                <div className="mx-auto max-w-7xl space-y-5">
                    <section className="rounded-3xl bg-white p-5 shadow-sm ring-1 ring-blue-100">
                        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                            <div className="flex items-center gap-4">
                                <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-[#E8F2FF] text-[#135491]">
                                    <FileText size={26} />
                                </div>

                                <div>
                                    <p className="text-xs font-bold uppercase tracking-[0.18em] text-[#135491]">
                                        Calidad
                                    </p>

                                    <h1 className="text-2xl font-black text-slate-900">
                                        Certificados
                                    </h1>

                                    <p className="text-sm text-slate-500">
                                        Administración de certificados registrados.
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

                    <section className="rounded-3xl bg-white p-4 shadow-sm ring-1 ring-blue-100">
                        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                            <div>
                                <h2 className="text-base font-black text-slate-900">
                                    Lista de certificados
                                </h2>

                                <p className="text-sm text-slate-500">
                                    Total de registros:{" "}
                                    <span className="font-bold text-[#135491]">
                                        {rows.length}
                                    </span>
                                </p>
                            </div>

                            <span className="w-fit rounded-full bg-blue-50 px-3 py-1 text-xs font-bold text-[#135491]">
                                Sistema activo
                            </span>
                        </div>

                        <div className="mt-4 overflow-x-auto rounded-2xl border border-slate-100">
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

                                <tbody className="divide-y divide-slate-100 bg-white">
                                    {rows.length === 0 ? (
                                        <tr>
                                            <td colSpan="6" className="px-5 py-14 text-center">
                                                <div className="mx-auto flex max-w-sm flex-col items-center">
                                                    <div className="mb-3 flex h-14 w-14 items-center justify-center rounded-2xl bg-blue-50 text-[#135491]">
                                                        <FileText size={28} />
                                                    </div>

                                                    <p className="font-bold text-slate-800">
                                                        No hay certificados registrados
                                                    </p>

                                                    <p className="mt-1 text-sm text-slate-500">
                                                        Crea uno nuevo para comenzar.
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                    ) : (
                                        rows.map((certificado) => (
                                            <tr
                                                key={certificado.id}
                                                className="transition hover:bg-[#F4F9FF]"
                                            >
                                                <td className="px-5 py-4">
                                                    <span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-bold text-[#135491]">
                                                        {certificado.code || "Sin clave"}
                                                    </span>
                                                </td>

                                                <td className="px-5 py-4">
                                                    <p className="max-w-[330px] truncate font-bold text-slate-900">
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
                                                        <ActionLink
                                                            href={route(
                                                                "admin.calidad.certificados.show",
                                                                certificado.id
                                                            )}
                                                            icon={<Eye size={15} />}
                                                            label="Ver"
                                                            tone="blue"
                                                        />

                                                        <ActionLink
                                                            href={route(
                                                                "admin.calidad.certificados.edit",
                                                                certificado.id
                                                            )}
                                                            icon={<Pencil size={15} />}
                                                            label="Editar"
                                                            tone="amber"
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

function ActionLink({ href, icon, label, tone = "blue" }) {
    const tones = {
        blue: "bg-blue-50 text-[#135491] hover:bg-[#135491] hover:text-white",
        amber: "bg-amber-50 text-amber-700 hover:bg-amber-500 hover:text-white",
    };

    return (
        <Link
            href={href}
            className={`inline-flex items-center gap-1 rounded-xl px-3 py-2 text-xs font-bold transition active:scale-95 ${tones[tone]}`}
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
