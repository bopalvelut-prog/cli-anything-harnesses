import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('import running')
@cli.command()
def start(): click.echo('import started')
if __name__ == '__main__': cli()
