import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zone running')
@cli.command()
def start(): click.echo('zone started')
if __name__ == '__main__': cli()
