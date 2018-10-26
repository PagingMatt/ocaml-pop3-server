open Pop3.Server
open Pop3.State
open Pop3.Store

module B = BackingStoreState (GmTimeBanner) (IrminStore)

module S = Server (B)

let () =
  let stop, _resolver = Lwt.wait () in
  Lwt_main.run (S.start ~hostname:"localhost" ~maildrop:"/tmp/maildrop" ~stop)