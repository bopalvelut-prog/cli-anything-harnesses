import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Alertmanager running')
@cli.command()
def silenced(): click.echo('Silenced alerts')
@cli.command()
def reload(): subprocess.run(['amtool', 'config', 'reload'])
if __name__ == '__main__': cli()
