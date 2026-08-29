import { cn } from "@/lib/utils";

interface RooftopDividerProps {
  className?: string;
  /** Flip the silhouette vertically, useful when closing out a section */
  flip?: boolean;
}

/**
 * Abstract rooftop / skyline silhouette — the page's signature motif.
 * Used behind the hero search box and as a quiet divider between sections.
 * Pure decoration: aria-hidden, no semantic content.
 */
export function RooftopDivider({ className, flip = false }: RooftopDividerProps) {
  return (
    <svg
      viewBox="0 0 1440 120"
      fill="none"
      preserveAspectRatio="none"
      aria-hidden="true"
      className={cn("w-full h-auto", flip && "-scale-y-100", className)}
    >
      <path
        d="M0 100 L60 100 L60 70 L110 70 L110 100 L180 100 L180 40 L200 20 L220 40 L220 100 L300 100 L300 60 L350 60 L350 100 L430 100 L430 80 L460 50 L490 80 L490 100 L560 100 L560 30 L590 10 L620 30 L620 100 L700 100 L700 65 L740 65 L740 100 L820 100 L820 45 L850 20 L880 45 L880 100 L950 100 L950 75 L990 75 L990 100 L1060 100 L1060 55 L1090 30 L1120 55 L1120 100 L1200 100 L1200 70 L1240 70 L1240 100 L1310 100 L1310 40 L1340 15 L1370 40 L1370 100 L1440 100 L1440 120 L0 120 Z"
        fill="currentColor"
      />
    </svg>
  );
}
