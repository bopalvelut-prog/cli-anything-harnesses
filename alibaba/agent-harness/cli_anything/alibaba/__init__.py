import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alibaba running')
@cli.command()
def start(): click.echo('alibaba started')
if __name__ == '__main__': cli()
