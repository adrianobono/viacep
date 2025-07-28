import click
from viacep.services import ViaCEPService
from viacep.exceptions import CEPLookupError

@click.group()
def main():
    """ViaCEP CLI - Brazilian Postal Code Lookup"""
    pass

@main.command()
@click.argument("cep")
def search(cep: str):
    """Search address information by CEP"""
    try:
        address = ViaCEPService.lookup_cep(cep)
        click.echo("Endereço encontrado:")
        click.echo(f"CEP: {address.cep}")
        click.echo(f"Rua: {address.street or 'N/A'}")
        click.echo(f"Complemento: {address.complement or 'N/A'}")
        click.echo(f"Bairro: {address.neighborhood or 'N/A'}")
        click.echo(f"Cidade: {address.city or 'N/A'}")
        click.echo(f"Estado: {address.state or 'N/A'}")
    except CEPLookupError as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise SystemExit(1)

if __name__ == "__main__":
    main()