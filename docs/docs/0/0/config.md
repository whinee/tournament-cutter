<h1 align="center" style="font-weight: bold">
    Configurations
</h1>

## **Config File**

### Config File Lookup Order of Precedence (CFLOP)

Hyaku is a cross-compatible project, which means that it could be ran in different OS. There is however a lack of unity in the standardization on the location of config files in this OSes. And such, I have devised a precedence order for Hyaku's config file in different platforms.

The following are the CFLOP for different OSes:

```mermaid
flowchart TD
    A([CFLOP]) --> L[--config argument]
        L --> B{OS?}
        B --> |*nix| C[./tc.yml]
            subgraph <br>
                C --> D{"XDG<br>CONFIG<br>HOME<br>(XCH)?"}
                D --> |true| E["${XCH}/tc/videos.yml"] --> F
                D --> |false| F["~/.config/tc/videos.yml"]
                F --> G["~/.tc"]
                G --> H["/etc/xdg/tc/videos.yml"]
                H --> I["/etc/tc/videos.yml"]
            end
        B --> |Windows| J[.\tc.yml]
            subgraph <br><br>
                J --> K["${boot drive}:\\<br>Users\${username}\<br>AppData\Roaming\Hyaku\<br>videos.yml"]
            end
```
