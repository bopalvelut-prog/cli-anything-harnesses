import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('KuCoin status')
@cli.command()
def balance(): click.echo('KuCoin balance')
if __name__ == '__main__': cli()
