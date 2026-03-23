import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auto running')
@cli.command()
def start(): click.echo('auto started')
if __name__ == '__main__': cli()
