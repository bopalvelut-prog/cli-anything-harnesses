import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Coolify started')
@cli.command()
def stop(): click.echo('Coolify stopped')
@cli.command()
def status(): click.echo('Coolify status')
if __name__ == '__main__': cli()
