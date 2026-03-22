import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Huobi status')
@cli.command()
def balance(): click.echo('Huobi balance')
if __name__ == '__main__': cli()
