import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dnsmasq running')
@cli.command()
def start(): click.echo('dnsmasq started')
if __name__ == '__main__': cli()
