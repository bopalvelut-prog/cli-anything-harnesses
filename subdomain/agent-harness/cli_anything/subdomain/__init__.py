import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('subdomain running')
@cli.command()
def start(): click.echo('subdomain started')
if __name__ == '__main__': cli()
