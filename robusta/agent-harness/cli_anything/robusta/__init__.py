import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def playbook(): click.echo('Robusta playbook')
@cli.command()
def triggers(): click.echo('Robusta triggers')
if __name__ == '__main__': cli()
