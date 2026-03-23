import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('regional running')
@cli.command()
def start(): click.echo('regional started')
if __name__ == '__main__': cli()
