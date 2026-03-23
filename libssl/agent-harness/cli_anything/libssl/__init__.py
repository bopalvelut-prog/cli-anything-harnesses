import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libssl running')
@cli.command()
def start(): click.echo('libssl started')
if __name__ == '__main__': cli()
