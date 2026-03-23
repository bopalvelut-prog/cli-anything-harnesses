import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dnsdist running')
@cli.command()
def start(): click.echo('dnsdist started')
if __name__ == '__main__': cli()
