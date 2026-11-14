---
name: "Design System"
version: "1.0.0"
colors:
  primary: "#2563EB"
  secondary: "#475569"
  accent: "#F59E0B"
  background: "#0F172A"
  surface: "#1E293B"
  textPrimary: "#F8FAFC"
  textSecondary: "#94A3B8"
  error: "#EF4444"
  success: "#10B981"
typography:
  fontFamily: "Inter, system-ui, -apple-system, sans-serif"
  headline:
    fontFamily: "Inter"
    fontWeight: 700
  body:
    fontFamily: "Inter"
    fontWeight: 400
spacing:
  unit: "4px"
  scale: [4, 8, 12, 16, 24, 32, 48, 64]
rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
elevation:
  sm: "0 1px 2px 0 rgb(0 0 0 / 0.05)"
  md: "0 4px 6px -1px rgb(0 0 0 / 0.1)"
---

# Design System

## Overview
A clean, accessible, modern interface focusing on dense, purposeful information architecture without visual noise. Designed to provide AI coding agents and human contributors with an authoritative, persistent source of truth.

## Colors & Semantic Roles
- **Primary (`#2563EB`)**: High-contrast blue reserved exclusively for primary interactive calls-to-action (CTAs) and active navigation states.
- **Secondary (`#475569`)**: Neutral slate used for secondary actions, subtle borders, and inactive UI elements.
- **Accent (`#F59E0B`)**: Amber accent for highlights, alerts, and feature badges.
- **Background (`#0F172A`)**: Deep dark foundation for page surfaces.
- **Surface (`#1E293B`)**: Raised surface container for cards, panels, and modals.
- **TextPrimary (`#F8FAFC`)**: High-contrast primary text meeting WCAG AAA contrast against surface/background.
- **TextSecondary (`#94A3B8`)**: Subdued text for metadata, captions, and secondary labels (meeting WCAG AA).
- **Error (`#EF4444`) / Success (`#10B981`)**: Semantic indicators for validation and system status.

## Typography Hierarchy
- **Font Stack**: `Inter`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif`.
- **Headings**: Semibold/Bold (`font-weight: 600` or `700`) with tight letter-spacing (`-0.02em`).
- **Body Text**: Regular (`font-weight: 400`), `16px` base (`line-height: 1.5`).
- **Small / Metadata**: `14px` or `12px` (`line-height: 1.4`).

## Layout & Spacing
- **Base Grid Unit**: `4px`.
- **Spacing Scale**: Multiples of 4/8 (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`).
- **Container Widths**: Mobile (`100%`), Tablet (`768px`), Desktop (`1200px` max).
- No arbitrary padding or margin values outside the defined spacing scale.

## Shapes & Elevation
- **Border Radius**: Cards and inputs use `rounded-md` (`8px`); buttons use `rounded-md` (`8px`) or `rounded-lg` (`16px`); pills and badges use `rounded-full`.
- **Elevation**: Flat by default with subtle border (`1px solid #334155`); floating elements (menus, modals) use `elevation.md`.

## Components & Signatures
- **Buttons**: Clear visual hierarchy (Primary filled, Secondary outline, Ghost for auxiliary actions). Minimum target size of 44x44px.
- **Form Inputs**: Distinct border in surface background, visible 2px focus ring using Primary color, inline error messages.
- **Modals / Dialogs**: Centered overlay on darkened backdrop, dismissible via Escape and click-outside.

## Do's and Don'ts
- **DO** use semantic design tokens instead of hardcoded hex values in component code.
- **DO** ensure all text/background combinations pass WCAG AA contrast (minimum 4.5:1 for normal text).
- **DO** maintain visual consistency across all newly generated views.
- **DON'T** introduce arbitrary padding, font families, or color variations outside this specification.
- **DON'T** mix sharp (0px) and rounded corners inconsistently across sibling components.
