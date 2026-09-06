# Ore Sight AI — Manganese Intelligence Platform

Frontend prototype for a Smart India Hackathon solution built for MOIL Limited.
This is a **frontend-only** build with realistic mock data, structured so a
FastAPI + ML backend can be plugged in later with minimal changes.

## Stack

React 18 · TypeScript · Vite · Tailwind CSS · hand-built shadcn-style UI
primitives · React Router · Recharts · react-map-gl / Mapbox GL JS · Axios ·
TanStack Query · Framer Motion · Lucide React.

## Getting started

```bash
npm install
cp .env.example .env      # optional — add a Mapbox token for the live GIS map
npm run dev
```

The app runs at `http://localhost:5173`.

### Mapbox token

The Reserve Intelligence page (`/reserves`) uses Mapbox GL JS via
`react-map-gl`. Add a free token from https://account.mapbox.com/ to
`VITE_MAPBOX_TOKEN` in `.env`. If no token is set, the page automatically
falls back to a static demo mine visualization instead of crashing — you'll
see a small "Mapbox token not configured" notice on the map.

## Project structure

```
src/
├── api/            Axios client + placeholder endpoint functions
│                    (getDashboardSummary, getReserveZones, authApi, etc.)
├── components/
│   ├── auth/        LoginForm, SignupForm, ProtectedRoute, AuthBrandPanel
│   ├── layout/      Sidebar, Header, PageContainer
│   ├── dashboard/   KPICard, ProductionChart, RiskSummary, AIInsightCard
│   ├── maps/        MineMap (+ Mapbox fallback), legend, controls, panel
│   ├── production/  ForecastChart, ProductionMetrics, ProductionDrivers
│   ├── risk/        RiskScore, RiskFactor, AlertCard, AlertTimeline
│   ├── recommendations/  RecommendationCard, ImpactCard
│   ├── operations/  EquipmentTable, EquipmentStatus, UtilizationChart
│   ├── satellite/   SatelliteMetrics, SatelliteMap
│   └── ui/          Hand-built Button, Card, Badge, Input, Progress, Dialog, etc.
├── context/
│   └── AuthContext.tsx   Session state — user, isAuthenticated, login/signup/logout
├── data/mock/       Typed mock data per domain (dashboard, reserves, ...)
├── hooks/           useToast (toast notification system)
├── lib/             cn(), formatters, tone/color helpers
├── pages/           One file per route (Landing, Login, Signup, ForgotPassword,
│                     Dashboard, Reserves, Production, Risks, Recommendations,
│                     Operations, Satellite, Settings)
├── types/           Shared TypeScript interfaces
├── App.tsx          Route table — public auth routes + protected AppShell routes
└── main.tsx         Providers (QueryClient, BrowserRouter, ToastProvider, AuthProvider)
```

## Routes

**Public:** `/` (landing), `/login`, `/signup`, `/forgot-password`

**Protected** (redirect to `/login` if not authenticated): `/dashboard`, `/reserves`,
`/production`, `/risks`, `/recommendations`, `/operations`, `/satellite`, `/settings`

## Authentication (frontend demo)

There's no real backend yet, so authentication is simulated in
`src/api/authApi.ts` using `localStorage` (keys: `oreSightAuthenticated`,
`oreSightUser`). `src/context/AuthContext.tsx` wraps that module and exposes
`user`, `isAuthenticated`, `login()`, `loginWithDemoAccount()`, `signup()` and
`logout()` to the rest of the app — no component talks to `localStorage`
directly.

**Demo account:** `demo@oresight.ai` / `demo123` (also available as a
one-click "Use Demo Account" button on the login page).

Signing up creates a local session from whatever the person typed into the
signup form — it does not create a real account anywhere.

`src/components/auth/ProtectedRoute.tsx` guards every workspace route and
redirects to `/login` when there's no active session.

### Swapping in real auth later

`authApi.ts` already reads `USE_MOCK_DATA` from `src/api/client.ts`, the same
flag the rest of the data layer uses. To connect FastAPI + JWT + PostgreSQL:

1. Implement `POST /auth/login`, `POST /auth/signup`, `POST /auth/logout` in
   FastAPI, returning `{ success, user }` (matching `AuthResult` in
   `src/types/index.ts`) or a JWT you attach via an `apiClient` interceptor.
2. Set `USE_MOCK_DATA = false`.
3. Delete the `localStorage` persistence calls in `authApi.ts` (or keep them
   as a token cache) — `AuthContext`, `ProtectedRoute`, `LoginForm`,
   `SignupForm` and the `Header`/`Sidebar` user info do not need to change.

## Connecting the FastAPI backend later

Every page reads data through a function in `src/api/*.ts`
(e.g. `getDashboardSummary`, `getReserveZones`, `getProductionForecast`,
`getRiskAnalysis`, `getRecommendations`, `getEquipmentStatus`,
`getSatelliteIndicators`). Each currently returns mock data via
`USE_MOCK_DATA` in `src/api/client.ts`.

To connect a real backend:

1. Set `VITE_API_BASE_URL` in `.env` to your FastAPI URL.
2. Flip `USE_MOCK_DATA` to `false` in `src/api/client.ts`.
3. Implement matching endpoints in FastAPI (paths are already written as
   comments/calls in each `*Api.ts` file, e.g. `GET /dashboard/summary`,
   `GET /reserves/zones`, `GET /production/forecast?range=30d`,
   `POST /recommendations/:id/apply`).
4. Response shapes should match the TypeScript interfaces in `src/types/index.ts`.

No component code needs to change — pages call the `*Api.ts` functions via
TanStack Query, not the mock data directly.

## Notes

- All data on every screen is **mock/demo data**, clearly marked with a
  "Prototype · Demo Data" indicator in the bottom of the app shell.
- Reserve map coordinates are fictional and do not represent actual
  confidential MOIL reserve locations.
- Satellite and reserve pages include an explicit disclaimer that surface
  indicators are supporting evidence only — subsurface reserve estimation
  requires geological and drilling data.
