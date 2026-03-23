import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shockwave running')
@cli.command()
def start(): click.echo('shockwave started')
if __name__ == '__main__': cli()
