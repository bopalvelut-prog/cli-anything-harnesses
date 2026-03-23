import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kendryte running')
@cli.command()
def start(): click.echo('kendryte started')
if __name__ == '__main__': cli()
