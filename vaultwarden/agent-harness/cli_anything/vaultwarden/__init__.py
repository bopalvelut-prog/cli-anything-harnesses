import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vaultwarden running')
@cli.command()
def start(): click.echo('vaultwarden started')
if __name__ == '__main__': cli()
