import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Ledger status')
@cli.command()
def accounts(): click.echo('Ledger accounts')
if __name__ == '__main__': cli()
